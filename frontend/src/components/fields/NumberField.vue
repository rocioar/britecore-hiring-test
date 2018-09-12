<template>
  <b-form-input
    v-model="inputValue"
    :id="id"
    type="number"
  />
</template>

<script>
import fieldMixin from './fieldMixin.js'

export default {
  mixins: [fieldMixin]
}
</script>
