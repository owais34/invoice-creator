import React, { useEffect } from 'react'
import { API } from '../api/config'
import { useParams } from 'react-router-dom';

const createMarkup = (htmlString) => {
  return { __html: htmlString };
};

function EditInvoiceTemplate() {
  let { id } = useParams();
  useEffect(() => {
  }, [])
  
  return (
    <div><h1>Edit invoice</h1>
        <div dangerouslySetInnerHTML={createMarkup("<h1>hello</h1>")}></div>
    </div>
  )
}

export default EditInvoiceTemplate