import React, {useState, useEffect} from 'react'
import { API } from '../api/config';
import { useNavigate } from 'react-router-dom';

function Home() {
  const [companies, setCompanies] = useState([]);
  const navigateTo = useNavigate()
  // Function to handle adding a new company
  const addCompany = () => {
    navigateTo("/addFirm")
  };


  useEffect(() => {
    API.get("/firm")
    .then(response=> {
      setCompanies(response.data.data)
    })
    .catch(err => console.log(err))
  
    return () => {
    }
  }, [])
  

  // Function to handle creating an invoice
  const createInvoice = (companyId) => {
    navigateTo(`/createInvoice/${companyId}`)
  };

  const deleteInvoice = (companyId) => {

  }
  
  const editInvoice = (companyId) => {
    navigateTo(`/editInvoiceTemplate/${companyId}`)
  }


  return (
    <div style={styles.app}>
      <header style={styles.header}>
        <h1>Invoice Creator</h1>
      </header>
      
      <div style={styles.companiesList}>
        <ul style={styles.companyList}>
          {companies.map((company) => (
            <li key={company.id} style={styles.companyItem}>
              {company.name}
              <button 
                onClick={() => createInvoice(company.id)} 
                style={styles.button}
              >
                Create Invoice
              </button>
              <button 
                onClick={() => deleteInvoice(company.id)} 
                style={styles.buttonRed}
              >
                Delete Invoice
              </button>
              <button 
                onClick={() => editInvoice(company.id)} 
                style={styles.buttonRed}
              >
                Edit Invoice Template
              </button>
            </li>
          ))}
        </ul>
      </div>

      <div style={styles.addCompany}>
        <button onClick={addCompany} style={styles.button}>
          Add Company
        </button>
      </div>
    </div>
  )
}

const styles = {
  app: {
    fontFamily: 'Arial, sans-serif',
    textAlign: 'center',
    padding: '20px',
  },
  header: {
    backgroundColor: '#282c34',
    color: 'white',
    padding: '20px',
  },
  companiesList: {
    marginTop: '20px',
  },
  companyList: {
    listStyleType: 'none',
    padding: 0,
  },
  companyItem: {
    margin: '10px 0',
  },
  button: {
    backgroundColor: '#4CAF50',
    color: 'white',
    border: 'none',
    padding: '10px 20px',
    cursor: 'pointer',
    marginLeft: '10px',
  },
  buttonRed: {
    backgroundColor: '#FFAACB',
    color: 'white',
    border: 'none',
    padding: '10px 20px',
    cursor: 'pointer',
    marginLeft: '10px',
  },
  buttonHover: {
    backgroundColor: '#45a049',
  },
  addCompany: {
    marginTop: '30px',
  },
  input: {
    padding: '8px',
    fontSize: '14px',
    marginRight: '10px',
    width: '200px',
  },
};

export default Home;
