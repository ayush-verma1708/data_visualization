document.addEventListener("DOMContentLoaded", function () {
  fetchDataAndRender();
});

async function fetchDataAndRender() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/get-data/");
    const data = await response.json();

    // Sort data based on likelihood in ascending order
    const sortedData = data.data.sort((a, b) => a.likelihood - b.likelihood);

    // Render data table
    renderDataTable(sortedData);

    // Render bar chart
    // renderBarChart(sortedData);

    //ScatterPlot
    // renderScatterPlot(sortedData);

    // const topicData = sortedData.filter((entry) => entry.topic === "YourTopic");
    // renderLineChart(topicData);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
  applyFilters();
}

function applyFilters() {
  const endYearFilter = document.getElementById("endYearFilter").value;

  // Fetch filtered data based on the end year
  fetch(`/filter_data?endYear=${endYearFilter}`)
    .then((response) => response.json())
    .then((filteredData) => {
      // Render the filtered data
      renderDataTable(filteredData);
      renderBarChart(filteredData);
      renderScatterPlot(filteredData);

      const topicData = filteredData.filter(
        (entry) => entry.topic === "YourTopic"
      );
      renderLineChart(topicData);
    })
    .catch((error) => {
      console.error("Error fetching filtered data:", error);
    });
}

function renderDataTable(data) {
  const tableBody = document.getElementById("data-table-body");
  tableBody.innerHTML = ""; // Clear existing data

  data.forEach((entry) => {
    const row = tableBody.insertRow();
    Object.values(entry).forEach((value) => {
      const cell = row.insertCell();
      cell.textContent = value;
    });
  });
}

// function renderBarChart(data) {
//   const labels = data.map((entry) => entry.country);
//   const relevanceData = data.map((entry) => entry.relevance);
//   const likelihoodData = data.map((entry) => entry.likelihood);

//   var ctx = document.getElementById("myChart-bar-country").getContext("2d");
//   var myChart = new Chart(ctx, {
//     type: "bar",
//     data: {
//       labels: labels,
//       datasets: [
//         {
//           label: "relevance",
//           data: relevanceData,
//           backgroundColor: "rgba(75, 192, 192, 0.2)",
//           borderColor: "rgba(75, 192, 192, 1)",
//           borderWidth: 1,
//         },
//         {
//           label: "likelihood",
//           data: likelihoodData,
//           backgroundColor: "rgba(75, 192, 192, 1)",
//           borderColor: "rgba(75, 192, 192, 1)",
//           borderWidth: 1,
//         },
//       ],
//     },
//     options: {
//       responsive: true,
//       scales: {
//         y: {
//           beginAtZero: true,
//         },
//       },
//     },
//   });
// }
