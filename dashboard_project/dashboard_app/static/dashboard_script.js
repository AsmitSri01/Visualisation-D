document.addEventListener('DOMContentLoaded', async () => {
    const data = await fetchData();
    updateVisualization(data);
});

async function fetchData() {
    const response = await fetch('data/');
    const data = await response.json();
    return data;
}

function updateVisualization(data) {
    console.log('Updating visualization with data:', data);
    // Remove previous visualization
    d3.select('#visualization').selectAll('*').remove();

    // Get selected filter values
    const endYear = document.getElementById('endYearFilter').value;
    const selectedTopic = document.getElementById('topicFilter').value;

    // Filter data based on selected values
    const filteredData = data.filter(item => {
        return (!endYear || item.end_year == endYear) &&
               (!selectedTopic || item.topic == selectedTopic);
        // Add similar conditions for other filters
    });

    // Use D3.js to create visualizations (replace this with your actual visualization code)
    const svg = d3.select('#visualization')
        .append('svg')
        .attr('width', 400)
        .attr('height', 200);

    svg.selectAll('rect')
        .data(filteredData)
        .enter()
        .append('rect')
        .attr('x', (d, i) => i * 50)
        .attr('y', d => 200 - d.intensity)
        .attr('width', 40)
        .attr('height', d => d.intensity)
        .attr('fill', 'blue');
}

// Add event listeners for filter changes
document.getElementById('endYearFilter').addEventListener('change', async () => {
    const data = await fetchData();
    updateVisualization(data);
});

document.getElementById('topicFilter').addEventListener('change', async () => {
    const data = await fetchData();
    updateVisualization(data);
});

// Repeat the above process for other filters
