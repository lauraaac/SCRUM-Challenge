<template>
  <v-app>
    <v-container>
      <v-list>
        <v-list-item-title class="text-h4 mb-4">
        Hi everyone, this is a little web page to get info about <br><br> some stocks and cryptocurrencies. <br><br> <br><br>Hope you enjoy!<br><br>
        </v-list-item-title>
        <v-list-item v-for="(item, index) in items" :key="item.id" class="mt-4">
          <v-list-item-content>
            <v-list-item-title class="mt-4">{{ item.name }}</v-list-item-title>
            <v-list-item-subtitle>{{ item.description }}</v-list-item-subtitle>
            <v-list-item v-if="index === 0" class="mt-4">
              <v-row justify="center">
                <v-col cols="12">
                  <v-btn 
                    color="primary" @click="redirectToStocksPage"
                  >Watch every stock</v-btn>
                </v-col>
              </v-row>
            </v-list-item>
            <v-list-item v-if="index === 1">
              <v-row justify="center">
                <v-col v-for="field in stockFields" :key="field.name" :cols="field.cols">
                  <v-select
                    v-if="field.name === 'Stock name'"
                    v-model="field.value"
                    :items="stockNames"
                    :label="field.name"
                  ></v-select>
                  <v-text-field v-else v-model="field.value" :label="field.name" class="short-text-field"></v-text-field>
                </v-col>
              </v-row>
              <v-row justify="center">
                <v-col cols="12">
                  <v-btn 
                    color="primary" @click="redirectToStockPage"
                  >Go to Stock</v-btn>
                </v-col>
              </v-row>
            </v-list-item>
            <v-list-item v-if="index === 2" class="mt-4">
              <v-row justify="center">
                <v-col cols="12">
                  <v-btn 
                    color="primary" @click="redirectToCryptosPage"
                  >Watch every cryptocurrency</v-btn>
                </v-col>
              </v-row>
            </v-list-item>
            <v-list-item v-if="index === 3">
              <v-row justify="center">
                <v-col v-for="field in cryptoFields" :key="field.name" :cols="field.cols">
                  <v-select
                    v-if="field.name === 'Crypto name'"
                    v-model="field.value"
                    :items="cryptoNames"
                    :label="field.name"
                    class="short-text-field"
                  ></v-select>
                  <v-text-field v-else v-model="field.value" :label="field.name" class="short-text-field"></v-text-field>
                </v-col>
              </v-row>
              <v-row justify="center">
                <v-col cols="12">
                  <v-btn color="primary" @click="redirectToCryptoPage">Go to Cryptocurrency</v-btn>
                </v-col>
              </v-row>
            </v-list-item>
          </v-list-item-content>
        </v-list-item>
        
      </v-list>
    </v-container>
  </v-app>
</template>

<script>

export default {
  data() {
    return {
      items: [
        {
          id: 1,
          name: 'All stocks',
          description: 'Nine stocks to view.',
        },
        {
          id: 2,
          name: 'Stocks by name and date ',
          description: 'Choose a stock in the boxes below and input dates in the following format: YYYY-MM-DD, if you wish, dates are optional.',
        },
        {
          id: 3,
          name: 'All cryptocurrencies',
          description: 'Seven cryptocurrencies to view.',
        },
        {
          id: 4,
          name: 'Cryptos by name and date',
          description: 'Choose a crypto in the box below and input dates in the following format: YYYY-MM-DD, if you wish, dates are optional.',
        },
      ],
      stockNames: [
        'Coca-Cola',
        'Apple',
        'Endava',
        'Globant',
        'IBM',
        'Amazon',
        'Meta',
        'Tesla',
        'Mercedes Benz',
      ],
      cryptoNames: [
        'Bitcoin',
        'Ethereum',
        'XRP',
        'BNB',
        'Cardano',
        'Dogecoin',
        'Solana',
      ],
      stockFields: [
        { name: 'Stock name', value: '', cols: 1 },
        { name: 'Start date', value: '', cols: 1 },
        { name: 'End date', value: '', cols: 1 },
      ],
      cryptoFields: [
        { name: 'Crypto name', value: '', cols: 1 },
        { name: 'Start date', value: '', cols: 1 },
        { name: 'End date', value: '', cols: 1 },
      ],
    };
  },
  methods: {
    redirectToStocksPage() {
      this.$router.push({
        path: '/stocks'
      });
    },
    redirectToStockPage() {
      this.$router.push({
        path: '/stock',
        query: {
          stockName: this.stockFields[0].value,
          startDate: this.stockFields[1].value,
          finishDate: this.stockFields[2].value,
        },
      });
    },
    redirectToCryptosPage() {
      this.$router.push({
        path: '/cryptos'
      });
    },
    redirectToCryptoPage() {
      this.$router.push({
        path: '/crypto',
        query: {
          cryptoName: this.cryptoFields[0].value,
          startDate: this.cryptoFields[1].value,
          finishDate: this.cryptoFields[2].value,
        },
      });
    },
  },
};
</script>

<style>
</style>