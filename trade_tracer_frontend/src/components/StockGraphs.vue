<template>
  <div class="chart-container">
    <div v-for="(stock, index) in stocks" :key="index" class="chart-wrapper">
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
    this.fetchStockUrls([
      'http://127.0.0.1:8000/stocks/',
      'http://127.0.0.1:8000/crypoCurrencies/',
      'http://127.0.0.1:8000/stocks/',
      'http://127.0.0.1:8000/crypoCurrencies/',
    ]);
  },
  methods: {
    fetchStockUrls(urls) {
      Promise.all(urls.map(url => fetch(url).then(response => response.json())))
        .then(data_array => {
          this.stocks = data_array;

          this.$nextTick(() => {
            data_array.forEach((data, index) => {
              const canvas = document.getElementById('canvas-' + index);
              const ctx = canvas.getContext('2d');

              Chart.register(LineController, LinearScale, PointElement, LineElement);

              const labels = data.stock_prices.map(stock => stock.date);
              const prices = data.stock_prices.map(stock => stock.price);

              new Chart(ctx, {
                type: 'line',
                data: {
                  labels: labels,
                  datasets: [
                    {
                      label: 'Stock price',
                      data: prices,
                      borderColor: 'green',
                      fill: true,
                    },
                  ],
                },
                options: {
                  responsive: false,
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