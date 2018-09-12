<template>
  <div>
    <b-form v-show="show">
      <b-form-group
        v-for='field in riskType.fields'
        :key="field.name"
        :label="field.name"
        :label-for="field.name"
      >
          <field
            :field="field"
            v-model="values[field.name]"
            :key="field.id"
          >
          </field>
      </b-form-group>
      <b-button type="submit" @click.prevent="showValues" variant="primary">Submit</b-button>
    </b-form>
  </div>
</template>

<script>
import RiskTypeField from '@/components/RiskTypeField'

import axios from 'axios'

export default {
  data: () => {
    return {
      riskType: {fields: []},
      show: false,
      values: {}
    }
  },

  created () {
    this.getRiskType()
  },

  methods: {
    getRiskType () {
      axios.get(
        `/risk_type/${this.$route.params.id}`
      ).then(response => {
        this.riskType = response.data
        this.show = true
      }).catch(error => {
        console.log(error)
      })
    },
    showValues () {
      console.log(this.values)
    }
  },

  components: {
    'field': RiskTypeField
  }
}
</script>
