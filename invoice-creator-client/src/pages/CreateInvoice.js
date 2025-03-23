import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom';
import { API } from '../api/config';


const RenderNormalForm = ({ sectionName, formFields, onChangeHandler }) => {
  return (
    <div key={sectionName}>
      <h2>{sectionName}</h2>
      {
        formFields.map((formField) => {
          if (formField.formAttributes["type"] === "file" || formField.formAttributes["type"] === "function")
            return null
          return (
            <div style={styles.formGroup} key={formField["field"]}>
              <label>{formField["description"]}</label>
              <input
                {...formField.formAttributes}
                name={formField["field"]}
                onChange={onChangeHandler}
                style={styles.input}
              />
            </div>
          )
        })
      }
    </div>
  )
}

const RenderTableForm = ({ sectionName, formFields, data, setData }) => {
  // Ignore the default onChangeHandler
  const colSpan = formFields.length - 1
  const [rows, setRows] = useState([])
  const [currentRow, setCurrentRow] = useState({
    "serialNumber": 1
  })
  const [total, setTotal] = useState(0)


  const onChangeHandler = (e) => {
    const { name, value, type } = e.target;
    setCurrentRow({
      ...currentRow,
      [name]: value,
    });
  }

  const onAddCurrentRow = (e) => {
    e.preventDefault()
    const newRows = [...rows]
    newRows.push(currentRow)
    let newTotal = 0
    newRows.forEach(({ amount }) => {
      newTotal += Number(amount)
    })
    setTotal(newTotal)
    setRows(newRows)
    setCurrentRow({
      "serialNumber": 1 + newRows.length
    })
    setData({
      ...data,
      [sectionName]: newRows
    })
  }

  const onDeleteCurrentRow = (e) => {
    e.preventDefault()
    const newRows = [...rows]
    newRows.splice(Number(e.target.value), 1)
    let newTotal = 0
    newRows.forEach((row, index) => {
      newTotal += Number(row["amount"])
      row["serialNumber"] = index + 1
    })
    setTotal(newTotal)
    setRows(newRows)
    setCurrentRow({
      "serialNumber": 1 + newRows.length
    })
    setData({
      ...data,
      [sectionName]: newRows
    })
  }

  const getDisplayedRow = (row, key) => {
    return <tr key={key}>
      {
        formFields.map(formField => <td key={formField["field"]} style={styles.cellStyle}>{row[formField["field"]]}</td>)
      }
      <td key={"addButton"} style={styles.cellStyle}><button value={key} onClick={onDeleteCurrentRow}>{"Delete"}</button></td>
    </tr>
  }

  return (
    <div key={sectionName}>
      <h2>{sectionName}</h2>
      <table style={styles.tableStyle}>
        <thead>
        <tr>
          {
            formFields.map(formField => <th key={formField["field"]} style={styles.headerStyle}>{formField["description"]}</th>)
          }
          <th key={"addButton"} style={styles.headerStyle}>{"Edit"}</th>
        </tr>
        </thead>
        <tbody>
        {
          rows.map((row, index) => getDisplayedRow(row, index))
        }
        <tr>
          { // this is the form section for the table
            formFields.map(formField => {
              return (
              <th key={formField["field"]} style={styles.cellStyle}>
                <input
                  {...formField.formAttributes}
                  value={currentRow[formField["field"]] ? currentRow[formField["field"]] : ""}
                  name={formField["field"]}
                  onChange={onChangeHandler}
                  style={styles.tableForminput}
                />
              </th>
              )
            })
          }
          <th key={"addButton"} style={styles.cellStyle}><button onClick={onAddCurrentRow}>{"Add"}</button></th>
        </tr>
        </tbody>
        <tfoot>
        <tr>
          <td style={styles.cellStyle} colSpan={colSpan}>Total</td>
          <td style={styles.cellStyle}>{total}</td>
        </tr>
        </tfoot>
      </table>
    </div>
  )
}


const RenderFormSection = ({ sectionName, formFields, onChangeHandler, data, setData }) => {
  if (!formFields)
    return null
  if (sectionName.startsWith("Table Details")) {
    return <RenderTableForm sectionName={sectionName}
      formFields={formFields}
      data={data} setData={setData} />
  } else {
    return <RenderNormalForm sectionName={sectionName} formFields={formFields} onChangeHandler={onChangeHandler} />
  }
}


function CreateInvoice() {
  let { id } = useParams();
  const [invoiceTemplate, setinvoiceTemplate] = useState({})
  const sectionOrder = ["General Information", "Table Details", "Table 2 Details", "Account Information", "Final Information"]
  const [data, setData] = useState({})
  const [loading, setLoading] = useState(false);
  const handleSubmit = (e) => {
    e.preventDefault()
    API.post(`/firm/${id}/generateInvoice`, data)
    .then(response => {
      // const tempElement = document.createElement('div');
      //   tempElement.innerHTML = response.data;

      //   // Use html2pdf to handle the conversion to PDF
      //   const options = {
      //     margin: 15,
      //     filename: `invoice_${new Date().getTime()}.pdf`,
      //     html2canvas: { scale: 2 },
      //     jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
      //   };

      //   // Convert the HTML to PDF and trigger download
      //   html2pdf()
      //     .from(tempElement)
      //     .set(options)
      //     .save();
      const newTab = window.open('', '_blank');  // This opens a new tab
      newTab.document.write(response.data); // Write the HTML to the new tab
      newTab.document.close(); // Ensure the document is fully loaded in the new tab
    })
    .catch(error => {
      console.error('There was an error!', error);
    });
  }

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    setData({
      ...data,
      [name]: value,
    });
  }

  useEffect(() => {
    API.get(`/firm/${id}/invoiceForm`)
      .then(resp => {
        setinvoiceTemplate(resp.data.data)
        const values = {}
        for (const section in resp.data.data) {
          if (section.startsWith("Table")) {
            continue
          }
          for (const fieldSpec of resp.data.data[section]) {
            let value = (fieldSpec["formAttributes"]["value"]) ? fieldSpec["formAttributes"]["value"] : ""
            if (fieldSpec["formAttributes"]["type"] === "autofill") {
              values[fieldSpec["field"]] = value
            }
          }
        }
        setData({
          ...values
        });
      })
      .catch(err => {
        console.log(err)
      })
  }, [])

  return (
    <div style={styles.container}>
      <header style={styles.header}>
        <h1>Create invoice</h1>
      </header>
      <div>
        <form onSubmit={handleSubmit} encType="multipart/form-data">
          {
            sectionOrder.map((sectionName) => {
              return <RenderFormSection
                key={sectionName}
                sectionName={sectionName}
                formFields={invoiceTemplate[sectionName]}
                onChangeHandler={handleChange}
                data={data} setData={setData} />
            })
          }
          <button type="submit" style={styles.button} disabled={loading} onSubmit={handleSubmit}>
            {loading ? 'Submitting...' : 'Create invoice'}
          </button>
        </form>
      </div>
    </div>
  )
}

const styles = {
  header: {
    backgroundColor: '#282c34',
    color: 'white',
    padding: '10px',
    textAlign: 'center'
  },
  formGroup: {
    marginBottom: '15px',
    textAlign: 'left',
  },
  input: {
    padding: '8px',
    width: '100%',
    fontSize: '14px',
    border: '1px solid #ccc',
    borderRadius: '4px',
  },
  tableForminput: {
    padding: '8px',
    width: '80%',
    fontSize: '14px',
    border: '1px solid #ccc',
    borderRadius: '4px',
  },
  container: {
    fontFamily: 'Arial, sans-serif',
    padding: '20px',
    maxWidth: '800px',
    margin: 'auto',
  },
  tableStyle: {
    width: '100%',
    borderCollapse: 'collapse',
    marginBottom: '20px',
  },
  headerStyle: {
    backgroundColor: '#f4f4f4',
    padding: '10px',
    textAlign: 'left',
    border: '1px solid #ddd',
  },
  cellStyle: {
    padding: '8px',
    textAlign: 'left',
    border: '1px solid #ddd',
  }
}

export default CreateInvoice