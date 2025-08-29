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
        <p>Review Analysis</p>
                {loading ? (
          <p style={{ fontSize: "16px" }}>conducting analysis of review...</p>
        ) : results ? (
          <div>
            <p style={{ fontSize: "16px" }}>Analysis Complete:</p>
            <div className="greyContainer">
               <p> Location: {results.location}</p>
               <p> by: {results.user}</p>
               <p> {results.review}</p>
            </div>
          </div>
        ) : (
          <p style={{ fontSize: "16px" }}>input a review above for analysis!</p>
        )}
        </div>
		</>
    );
}
