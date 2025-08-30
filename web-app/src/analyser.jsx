import * as React from 'react';
import ReviewForm from './components/ReviewForm';
import './App.css'

export default function ReviewAnalyser() {
    const [results, setResults] = React.useState(null);
    const [loading, setLoading] = React.useState(false);
    
    return (
		<>
        <div>
        <ReviewForm setResults={setResults} setLoading={setLoading} />
        </div>
        
        <div className="pageContainer">
        <h4>Review Analysis</h4>
                {loading ? (
          <p>conducting analysis of review...</p>
        ) : results ? (
          <div>
            <p>✅Analysis Complete:</p>
            <div className="greyContainer">
               <p> {results.review}</p>
            </div>
          </div>
        ) : (
          <p style={{ fontSize: "16px", fontWeight: "normal" }}>input a review above for analysis!</p>
        )}
        </div>
		</>
    );
}
