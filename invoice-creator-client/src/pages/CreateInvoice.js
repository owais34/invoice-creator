import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom';
import { API, BASE_URL } from '../api/config';

const renderFormSection = (sectionName , formFields, onChangeHandler) => {
  return (
    <>
    <h2>{sectionName}</h2>
    
    </>
  )
}


function CreateInvoice() {
  let { id } = useParams();
  const [invoiceTemplate, setinvoiceTemplate] = useState({})
  const sectionOrder = ["General Information", "Table Details", "Table 2 Details", "Account Information", "Final Information"]
  const [data, setData] = useState({})
  const [loading, setLoading] = useState(false);
  const handleSubmit = () => {

  }

  useEffect(() => {
    API.get(`/firm/${id}/invoiceForm`)
    .then(resp => {
      setinvoiceTemplate(resp.data.data)
      for (const section in resp.data.data) {
        for (const fieldSpec in resp.data.data[section]) {
          let value = fieldSpec["formAttributes"]["value"] ? fieldSpec["formAttributes"]["value"] : ""
          setData({
            ...data,
            [fieldSpec["field"]]: value
          });
        }
      }
    })
    .catch(err => {
      console.log(err)
    })
  }, [])
  
  return (
    <div>
      <header style={styles.header}>
        <h1>Create invoice</h1>
      </header>
      <div>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        {
          sectionOrder.map((sectionName) => { 
              return renderFormSection(sectionName, invoiceTemplate[sectionName], )
          })
        }
      <button type="submit" style={styles.button} disabled={loading}>
          {loading ? 'Submitting...' : 'Add Firm'}
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
  }
}

export default CreateInvoice