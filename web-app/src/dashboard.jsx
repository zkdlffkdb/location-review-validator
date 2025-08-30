import './App.css';
import MetricsChart from './components/metricschart';

export default function Dashboard() {
    return (
        <>
        <div>
        <h1>Analytics Dashboard</h1>
        <p>Comprehensive insights into review quality, policy violations, and system performance across all analysed locations</p>
        </div>

        <div className="pageContainer">
        <h4 className="graphs">Model Performance</h4>
        <p className="graphs">overall</p>
        <div style={{display: "flex", flexDirection: "row"}}>
        
        <div className="pageContainer">
        <p>accuracy</p>
        <p style={{color: "#ff746c", fontWeight: "bold"}}>84%</p>
        </div>
        
        <div className="pageContainer">
        <p>precision</p>
        <p style={{color: "#8884d8", fontWeight: "bold"}}>84%</p>
        </div>
        
        <div className="pageContainer">
        <p>recall</p>
        <p style={{color: "#82ca9d", fontWeight: "bold"}}>84%</p>
        </div>
        
        <div className="pageContainer">
        <p>f1</p>
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
