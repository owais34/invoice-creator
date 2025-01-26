import React from 'react';
import { Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import AddFirm from './pages/AddFirm';
import CreateInvoice from './pages/CreateInvoice';
import EditInvoiceTemplate from './pages/EditInvoiceTemplate';


function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/addFirm" element={<AddFirm/>} />
        <Route path="/createInvoice/:id" element={<CreateInvoice/>} />
        <Route path="/editInvoiceTemplate/:id" element={<EditInvoiceTemplate/>} />
      </Routes>
    </>
  );
}

export default App;
