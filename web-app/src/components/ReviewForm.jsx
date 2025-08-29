import styles from "./ReviewForm.module.css";
import { React, useState } from "react";

function ReviewForm({setResults, setLoading}) {
  const [loc, setLoc] = useState("");
  const [username, setUsername] = useState("");
  const [review, setReview] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(loc, username, review);

    setLoading(true)
    // add form logic to send input into ML machine / backend
    // Simulate async backend call (replace with fetch/axios later)
    setTimeout(() => {
      setResults({
        location: loc,
        user: username || "Anonymous",
        review: review,
      });
      setLoading(false);
    }, 2000);
  };


  return (
    <div className={styles.pageContainer}>
      <h1 className={styles.title}>Review Analyser</h1>
      <p className={styles.para}>
        enter a review and location details for analysis.
      </p>
      <fieldset className={styles.fieldset}>
        <form className={styles.form} onSubmit={handleSubmit} method="get">
          <div className={styles.formContainer}>
            <div className={styles.row}>
              <div className={styles.fieldGroup}>
                <label htmlFor="loc">Location*</label>
                <input
                  type="text"
                  name="loc"
                  id="loc"
                  value={loc}
                  onChange={(e) => setLoc(e.target.value)}
                  placeholder=" enter location"
                  required
                  className={styles.shortinput}
                />
              </div>
              <div className={styles.fieldGroup}>
                <label htmlFor="username">Username (optional)</label>
                <input
                  type="text"
                  name="username"
                  id="username"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  placeholder=" enter username"
                  className={styles.shortinput}
                />
              </div>
            </div>

            <div className={styles.fieldGroup}>
              <label htmlFor="review">Review*</label>
              <textarea
                name="review"
                id="review"
                value={review}
                onChange={(e) => setReview(e.target.value)}
                placeholder=" enter review"
                required
                className={styles.input}
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
