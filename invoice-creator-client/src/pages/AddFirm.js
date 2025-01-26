import React, { useEffect, useState } from 'react';
import { API } from '../api/config';

function AddFirm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    shortDescription: '',
    phoneNumber: '',
    addressLine1: '',
    addressLine2: '',
    addressLine3: '',
    gstinNumber: '',
    logoImage: null
  });
  const [formFields, setFormFields] = useState([])

  useEffect(() => {
    API.get("/firm/form")
    .then(resp => {
      setFormFields(resp.data.data)
    })
    .catch(err => {
      console.log(err)
      alert("Something went wrong !!")
    })
  }, [])
  
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState('');

  const handleChange = (e) => {
    const { name, value, type } = e.target;
    if (type === "file") {
      setFormData({
        ...formData,
        [name]: e.target.files[0]
      })
    } else {
    setFormData({
      ...formData,
      [name]: value,
    });
  }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formDataToSend = new FormData();
    formFields.forEach(({field}) => {
      if (formData[field])
      formDataToSend.append(field, formData[field])
    })
    setLoading(true);
    setError(null);
    setSuccessMessage('');

    try {
      const response = await API.post('/firm', formDataToSend, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status === 201) {
        setSuccessMessage('Firm created successfully!');
        setFormData({
        });
      }
    } catch (err) {
      setError('Error creating firm. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h2>Add Firm</h2>
      {successMessage && <div style={styles.success}>{successMessage}</div>}
      {error && <div style={styles.error}>{error}</div>}
      
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        {
          formFields.map((formField) => {
            return (
              <div style={styles.formGroup}>
              <label>{formField["description"]}</label>
              <input
                {...formField.formAttributes}
                name={formField["field"]}
                onChange={handleChange}
                style={styles.input}
              />
            </div>
            )
          })
        }
        <button type="submit" style={styles.button} disabled={loading}>
          {loading ? 'Submitting...' : 'Add Firm'}
        </button>
      </form>
    </div>
  );
}

const styles = {
  container: {
    fontFamily: 'Arial, sans-serif',
    padding: '20px',
    maxWidth: '600px',
    margin: 'auto',
  },
  formGroup: {
    marginBottom: '15px',
    textAlign: 'left',
  },
  label: {
    fontWeight: 'bold',
  },
  input: {
    padding: '8px',
    width: '100%',
    fontSize: '14px',
    border: '1px solid #ccc',
    borderRadius: '4px',
  },
  button: {
    backgroundColor: '#4CAF50',
    color: 'white',
    padding: '10px 20px',
    border: 'none',
    cursor: 'pointer',
    fontSize: '16px',
    borderRadius: '4px',
  },
  success: {
    color: 'green',
    marginBottom: '10px',
  },
  error: {
    color: 'red',
    marginBottom: '10px',
  },
};

export default AddFirm;
