import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import './App.css'
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
        // event.type can be equal to focus with selectionFollowsFocus.
        if (
            event.type !== 'click' ||
            (event.type === 'click' && samePageLinkNavigation(event))
        ) {
            setValue(newValue);
        }
    };

    return (
        <>
        <Box sx={{ width: '100%' }}>
        
        <Tabs value={value} onChange={handleChange}>
        <Tab label="Review Analyser" />
        <Tab label="Sample Reviews" />
        <Tab label="Analytics Dasboard" />
        </Tabs>

            {value === 2 && <Dashboard />}
        </Box>
        </>
    )
}

export default App
