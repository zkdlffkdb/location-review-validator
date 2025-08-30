import styles from "./ReviewForm.module.css";
import { React, useState } from "react";

function ReviewForm({ setResults, setLoading }) {
  const [loc, setLoc] = useState("");
  const [username, setUsername] = useState("");
  const [file, setFile] = useState(null);
  const url = "http://127.0.0.1:5000/predict";

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please upload a JSON file containing your review.");
      return;
    }

    setLoading(true);

    try {
      const text = await file.text();
      const jsonData = JSON.parse(text);

      console.log("Parsed JSON:", jsonData);

      // Send the request to the Flask API
      const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const responseData = await response.json();
        console.log(response);
        console.log(responseData);
      // Update the results with the API response
      setResults({
        review: jsonData.review_text,
        prediction: responseData.prediction,
      });
      
    } catch (error) {
      console.error("Error processing file:", error);
      alert("Invalid JSON or server error: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.pageContainer}>
      <h1 className={styles.title}>Review Analyzer</h1>
      <p className={styles.para}>
        Submit a .json file in the following format for analysis:
      </p>
      <pre style={{ marginTop: '0px' }}>
        {`
        {
          "review_text": string,
          "rating_person": number [0.0,5.0],
          "main_category": string,
          "can_claim": number, {0|1},
          "is_local_guide": number, {0|1},
          "sentiment_polarity": number [0.0,1.0],
          "sentiment_subjectivity": number [0.0,1.0]
        }
        `}
      </pre>
      <fieldset className={styles.fieldset}>
        <form className={styles.form} onSubmit={handleSubmit}>
          <div className={styles.formContainer}>
            <div className={styles.row}>
              {/* Your form fields here */}
            </div>

            <div className={styles.fieldGroup}>
              <label htmlFor="file">JSON file containing review*</label>
              <input
                type="file"
                accept=".json"
                name="file"
                id="file"
                onChange={(e) => setFile(e.target.files[0])}
                required
              />
            </div>

            <div className={styles.buttonRow}>
              <button type="submit" className={styles.button}>
                Submit
              </button>
            </div>
          </div>
        </form>
      </fieldset>
    </div>
  );
}

export default ReviewForm;
/*
import styles from "./ReviewForm.module.css";
import { React, useState } from "react";

function ReviewForm({setResults, setLoading}) {
  const [loc, setLoc] = useState("");
  const [username, setUsername] = useState("");
  const [file, setFile] = useState(null);
  const url = "http://127.0.0.1:5000/predict";

const handleSubmit = async (e) => {
  e.preventDefault();

  if (!file) {
    alert("please upload a JSON file containing your review.");
    return;
  }

  setLoading(true);

  try {
    const text = await file.text(); 
    const jsonData = JSON.parse(text);

    console.log("Parsed JSON:", jsonData);

    // simulate async backend
    setTimeout(() => {
      setResults({
        review: jsonData.review_text,
      });
      setLoading(false);
    }, 2000);

  } catch (error) {
    console.error("error processing file:", error);
    alert("invalid JSON or server error");
    setLoading(false);
  }
};

  return (
    <div className={styles.pageContainer}>
      <h1 className={styles.title}>Review Analyser</h1>
       <p className={styles.para}>
        submit a .json file in the following format for analysis:
      </p>
      <pre style={{marginTop:'0px'}}>
      {`
      {
    "review_text": string,
    "rating_person": number [0.0,5.0],
    "main_category": string,
    "can_claim": number, {0|1},
    "is_local_guide": number, {0|1},
    "sentiment_polarity": number [0.0,1.0],
    "sentiment_subjectivity": number [0.0,1.0]
    }
      `}
      </pre>
      <fieldset className={styles.fieldset}>
        <form className={styles.form} onSubmit={handleSubmit}>
          <div className={styles.formContainer}>
            <div className={styles.row}>
            </div>

            <div className={styles.fieldGroup}>
              <label htmlFor="file">JSON file containing review*</label>
              <input
                type="file"
                accept=".json"
                name="file"
                id="file"
                onChange={(e) => setFile(e.target.files[0])}
                required
              />
            </div>

            <div className={styles.buttonRow}>
              <button type="submit" className={styles.button}>
                Submit
              </button>
            </div>
      </div>
        </form>
      </fieldset>
    </div>
  );
}

export default ReviewForm;
*/
