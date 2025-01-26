const express = require('express');
const firmRouter = require('./routes/firm');
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

app.use("api/v1/firm", firmRouter)

// Start the server
const PORT = process.env.PORT || 5000;


app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
