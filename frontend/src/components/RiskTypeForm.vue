<template>
  <div>
    <b-form v-show="show">
        <b-form-group v-show="show" v-for='field in riskType.fields' :key="field.name"
                    :label="field.name" :label-for="field.name">
            <b-form-input :id="field.name" type="text">
            </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data: () => {
    return {
      riskType: {fields: []},
      show: false
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
    }
  }
}
</script>
