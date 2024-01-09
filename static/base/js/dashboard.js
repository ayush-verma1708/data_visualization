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
    renderBarChart(sortedData);

    // Render pie chart
    renderPieChart(sortedData);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
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

function renderBarChart(data) {
  const labels = data.map((entry) => entry.city);
  const intensityData = data.map((entry) => entry.likelihood);

  var ctx = document.getElementById("myChart-bar-city").getContext("2d");
  var myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Intensity",
          data: intensityData,
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          borderColor: "rgba(75, 192, 192, 1)",
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

function renderPieChart(data) {
  const ctx = document.getElementById("myChart-pie-topic").getContext("2d");

  // Extract unique topics
  const uniqueTopics = [...new Set(data.map((entry) => entry.topic))];

  // Calculate the total relevance for each topic
  const topicRelevances = uniqueTopics.map((topic) => {
    const topicData = data.filter((entry) => entry.topic === topic);
    const totalRelevance = topicData.reduce(
      (sum, entry) => sum + parseFloat(entry.relevance),
      0
    );
    return {
      topic: topic,
      totalRelevance: totalRelevance,
    };
  });

  const myChart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: topicRelevances.map((entry) => entry.topic),
      datasets: [
        {
          data: topicRelevances.map((entry) => entry.totalRelevance),
          backgroundColor: topicRelevances.map(() => getRandomColor()),
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          position: "top",
        },
      },
    },
  });
}

// Function to generate a random color for chart segments
function getRandomColor() {
  const letters = "0123456789ABCDEF";
  let color = "#";
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}
