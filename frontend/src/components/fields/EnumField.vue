<template>
  <b-form-select
    v-model="inputValue"
    :id="id"
    :options="options"
    class="mb-3"
  />
</template>

<script>
import fieldMixin from './fieldMixin.js'

export default {
  mixins: [fieldMixin]
}
</script>
