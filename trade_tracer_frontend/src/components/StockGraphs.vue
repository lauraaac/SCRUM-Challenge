<template>
  <div class="chart-container">
    <div v-for="(stockData, index) in stocks" :key="index" class="chart-wrapper">
      <h2>{{ stockData[0].name }}</h2>
      <canvas :id="'canvas-' + index" class="chart-canvas"></canvas>
    </div>
  </div>
</template>

<script>
import { Chart, LineController, LinearScale, PointElement, LineElement } from 'chart.js/auto';

export default {
  data() {
    return {
      stocks: [],
    };
  },
  mounted() {
    const stockNames = ['Coca-Cola', 'Apple', 'Endava', 'Globant', 'IBM', 'Amazon', 'Meta', 'Tesla', 'Mercedes Benz'];
    const baseUrl = 'http://127.0.0.1:8000/';

    const urls = stockNames.map(name => `${baseUrl}stocks/?name=${name}`);

    this.fetchStockUrls(urls);
  },
  methods: {
    fetchStockUrls(urls) {
      Promise.all(urls.map(url => fetch(url).then(response => response.json())))
        .then(dataArray => {
          this.stocks = dataArray;

          this.$nextTick(() => {
            dataArray.forEach((data, index) => {
              const canvas = document.getElementById('canvas-' + index);
              const ctx = canvas.getContext('2d');

              Chart.register(LineController, LinearScale, PointElement, LineElement);

              const labels = data.map(stock => stock.date);
              const prices = data.map(stock => parseFloat(stock.price));
              const colors = ['#ed0109', '#fafafa', '#de411b', '#c0d732', '#406cac', '#febd69', '#0064e0', '#e82127', '#c2c5ca'];

              new Chart(ctx, {
                type: 'line',
                data: {
                  labels: labels,
                  datasets: [
                    {
                      label: 'Stock price',
                      data: prices,
                      borderColor: colors[index % colors.length],
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
            });
          });
        });
    },
  },    
};
</script>

<style>
.chart-container {
  display: flex;
  flex-wrap: wrap;
}

.chart-wrapper {
  margin: 10px;
}

.chart-canvas {
  width: 456px;
  height: 356px;
}
</style>
