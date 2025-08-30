import React from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

const data = [
  { name: "Advertisement", precision: 0.75, recall: 0.75, f1: 0.75},
  { name: "Irrelevant content", precision: 0.80, recall: 0.67, f1: 0.73},
  { name: "Rants without visit", precision: 0.48, recall: 0.34, f1: 0.40},
  { name: "Relevant", precision: 0.90, recall: 0.69, f1: 0.78},
  { name: "Relevant + quality", precision: 0.78, recall: 0.91, f1: 0.84},
  { name: "Vague", precision: 0.68, recall: 1.00, f1: 0.81},
  { name: "No review", precision: 0.94, recall: 1.00, f1: 0.97},
];

export default function MetricsChart() {
  return (
    <ResponsiveContainer width="100%" height={500}>
      <BarChart
        data={data}
        margin={{ top: 20, right: 30, left: 20, bottom: 60 }}
      >
        <XAxis dataKey="name" fontSize="16px" interval={0} />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="precision" fill="#8884d8" />
        <Bar dataKey="recall" fill="#82ca9d" />
        <Bar dataKey="f1" fill="#ffc658" />
      </BarChart>
    </ResponsiveContainer>
  );
}
