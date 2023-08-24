<template>
    <div class="chart-container">
      <div v-for="(cryptoData, index) in cryptos" :key="index" class="chart-wrapper">
        <h2>{{ cryptoData[0].name }}</h2>
        <canvas :id="'canvas-' + index" class="chart-canvas"></canvas>
      </div>
  </div>
</template>

<script>
import { Chart, LineController, LinearScale, PointElement, LineElement } from 'chart.js/auto';

export default {
  data() {
    return {
      cryptos: [],
    };
  },
  mounted() {
    const cryptoNames = ['Bitcoin', 'Ethereum', 'XRP', 'BNB', 'Cardano', 'Dogecoin', 'Solana'];
    //const cryptoNames = ['Bitcoin', 'Ethereum', 'XRP', 'BNB', 'Cardano'];
    const baseUrl = 'http://127.0.0.1:8000/';

    const urls = cryptoNames.map(name => `${baseUrl}cryptos/?name=${name}`);

    this.fetchCryptoUrls(urls);
  },
  methods: {
    fetchCryptoUrls(urls) {
      Promise.all(urls.map(url => fetch(url).then(response => response.json())))
        .then(dataArray => {
          this.cryptos = dataArray;

          this.$nextTick(() => {
            dataArray.forEach((data, index) => {
              const canvas = document.getElementById('canvas-' + index);
              const ctx = canvas.getContext('2d');

              Chart.register(LineController, LinearScale, PointElement, LineElement);

              const labels = data.map(crypto => crypto.date);
              const prices = data.map(crypto => parseFloat(crypto.price));
              const colors = ['#f7931a', '#1d1e1e', '#22282e', '#f0b809', '#0336b3', '#bca133', '#2eeccb'];

              new Chart(ctx, {
                type: 'line',
                data: {
                  labels: labels,
                  datasets: [
                    {
                      label: 'Crypto price',
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