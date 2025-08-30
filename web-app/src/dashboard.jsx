import './App.css';
import MetricsChart from './components/metricschart';

export default function Dashboard() {
    return (
        <>
        <div>
        <h1>Analytics Dashboard</h1>
        <p>Comprehensive insights into review quality, policy violations, and system performance across all analysed locations</p>
        </div>
        
        <div style={{display: "flex", flexDirection: "row", gap: "20px"}}>

        <div className="pageContainer">
        <h4 className="graphs">Total Reviews</h4>
        <p className="graphs">3,438</p>
        </div>

        <div className="pageContainer">
        <h4 className="graphs">Top location category</h4>
        <p className="graphs">Restaurant</p>
        </div>

        <div className="pageContainer">
        <h4 className="graphs">"relevant and quality" reviews</h4>
        <p className="graphs">966</p>
        </div>

        </div>
        
        <div className="pageContainer">
        <h4 className="graphs">Model Performance</h4>
        <p className="graphs">overall</p>
        <div style={{display: "flex", flexDirection: "row"}}>
        
        <div className="pageContainer">
        <p className="graphs">accuracy</p>
        <p style={{color: "#ff746c", fontWeight: "bold"}}>84%</p>
        </div>
        
        <div className="pageContainer">
        <p className="graphs">precision</p>
        <p style={{color: "#8884d8", fontWeight: "bold"}}>84%</p>
        </div>
        
        <div className="pageContainer">
        <p className="graphs">recall</p>
        <p style={{color: "#82ca9d", fontWeight: "bold"}}>84%</p>
        </div>
        
        <div className="pageContainer">
        <p className="graphs">f1</p>
        <p style={{color: "#ffc658", fontWeight: "bold"}}>83%</p>
        </div>
        
        </div>
        </div>
            <div className="pageContainer">
            <h4 className="graphs">Model Performance</h4>
            <p className="graphs">by review classifications</p>
            <MetricsChart />
        </div>
        </>
    );
}
