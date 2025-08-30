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
        <div className="pageContainer" />
        </div>
            <div className="pageContainer">
            <h4 className="graphs">Model Performance</h4>
            <p className="graphs">by review classifications</p>
            <MetricsChart />
        </div>
        </>
    );
}
