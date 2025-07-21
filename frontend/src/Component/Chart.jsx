import React from "react";
import {Bar} from 'react-chartjs-2'
import { Chart as ChartJS, BarElement, CategoryScale, LinearScale, Tooltip, Legend} from 'chart.js'

ChartJS.register(CategoryScale, LinearScale, BarElement, Tooltip, Legend)

const Chart = () => {

    const data = {
        labels: ['Phishing', 'Legitimate'],
        datasets: [
            {
                label: 'Phishing Confidence',
                data: [80, 20], // *0% phishing confidence
                backgroundColor: ['rgba(0, 0, 0, 0.56)', 'rgba(210, 160, 7, 0.62)'],
                borderWidth: 2
            },
        ] ,
    }

    const options = {
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
            }
        }
    }

    return (
        <div className="" style={{maxWidth: '900px'}}>
            <Bar data={data} options={options} />
        </div>
    )
}

export default Chart;