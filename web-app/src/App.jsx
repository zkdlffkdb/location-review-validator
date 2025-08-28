import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import './App.css'
import ReviewAnalyser from './analyser';
import SampleReviews from './sample';
import Dashboard from './dashboard';

function samePageLinkNavigation(event) {
	if (
		event.defaultPrevented ||
		event.button !== 0 || // ignore everything but left-click
		event.metaKey ||
		event.ctrlKey ||
		event.altKey ||
		event.shiftKey
	) {
		return false;
	}
	return true;
}

function App() {
	const [count, setCount] = React.useState(0)
	const [value, setValue] = React.useState(0);

	const handleChange = (event, newValue) => {
		if (
			event.type !== 'click' ||
			(event.type === 'click' && samePageLinkNavigation(event))
		) {
			setValue(newValue);
		}
	};

	return (
		<>
		<div
		style={{
			width: "100%",           
			display: "flex",
			justifyContent: "center",
			flexDirection: "column",
			marginLeft: "28%",
			backgroundColor: "#DDECFF",
		}}
		>
		<h1>Intelligent Review Quality & Relevancy Detection</h1>
		<Tabs value={value} onChange={handleChange} variant="fullWidth">
		<Tab label="Review Analyser" />
		<Tab label="Sample Reviews" />
		<Tab label="Analytics Dashboard" />
		</Tabs>

		{value === 0 && <ReviewAnalyser />}
		{value === 1 && <SampleReviews />}
		{value === 2 && <Dashboard />}
		</div>
		</>
	)
}

export default App
