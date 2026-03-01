const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.post("/predict", (req, res) => {
    const year = req.body.year;

    if (!year) {
        return res.status(400).json({ error: "Year is required" });
    }

    const scriptPath = path.join(
        __dirname,
        "../ml-model/predict.py"
    );

    exec(`python "${scriptPath}" ${year}`, (error, stdout, stderr) => {
        if (error) {
            console.error(error);
            return res.status(500).json({ error: "Prediction failed" });
        }

        res.json({ result: stdout.trim() });
    });
});

app.listen(5000, () => {
    console.log("Server running on http://localhost:5000");
});