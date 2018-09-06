<template>
  <b-list-group>
    <b-list-group-item v-for='riskType in riskTypes' :key="riskType.name">
      <b-link :to="{name: 'risk-type-form', params: { id: riskType.id }}">{{ riskType.name  }}</b-link>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import axios from 'axios'

export default {
  data: () => {
    return {
      riskTypes: []
    }
  },

  created () {
    this.getRiskTypes()
  },

  methods: {
    getRiskTypes () {
      axios.get(
        '/risk_type/'
      ).then(response => {
        this.riskTypes = response.data
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
