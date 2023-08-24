<template>
  <div class="single-graph-container">
    <div class="center-content">
      <h2>{{ this.$route.query.stockName }}</h2>
      <canvas ref="chartCanvas" class="chart-canvas"></canvas>
    </div>
  </div>
</template>

<script>
import { Chart, LineController, LinearScale, PointElement, LineElement } from 'chart.js/auto';

export default {
  mounted() {
    this.fetchStockData();
  },
  methods: {
    fetchStockData() {
      try {
        const data = this.fetchDataFromServer();
        this.renderChart(data);
      } catch (error) {
        console.error('Error fetching stock data:', error);
      }
    },
    fetchDataFromServer() {
      let url = `http://127.0.0.1:8000/stocks/?name=${this.$route.query.stockName}`;

      if (this.$route.query.startDate) {
        url += `&startDate=${this.$route.query.startDate}`
      }
      
      if (this.$route.query.finishDate) {
        url += `&finishDate=${this.$route.query.finishDate}`
      }

      const xhr = new XMLHttpRequest();
      xhr.open('GET', url, false); // The third parameter "false" makes the request synchronous
      xhr.send();

      if (xhr.status === 200) {
        return JSON.parse(xhr.responseText);
      } else {
        throw new Error(`Request failed with status ${xhr.status}`);
      }
    },
    renderChart(data) {
      const canvas = this.$refs.chartCanvas;
      const ctx = canvas.getContext('2d');

      Chart.register(LineController, LinearScale, PointElement, LineElement);

      const labels = data.map(stock => stock.date);
      const prices = data.map(stock => parseFloat(stock.price));
      const color = '#de411b';

      new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Stock price',
              data: prices,
              borderColor: color,
              fill: true,
            },
          ],
        },
        options: {
          responsive: false,
          plugins: {
            tooltip: {
              enabled: true,
              callbacks: {
                label: context => `Value: ${context.formattedValue}`,
              },
            },
          },
        },
      });
    },
  },
};
</script>

<style>
.single-graph-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.center-content {
  text-align: center;
}
</style>