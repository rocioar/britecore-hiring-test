<template>
  <component
    :id="field.id"
    :is="fieldTypeToComponent(field.field_type)"
    :options="field.options"
    v-model="inputValue"
  />
</template>

<script>
import {
  TextField,
  NumberField,
  DateField,
  EnumField
} from '@/components/fields'

const fieldTypeToComponentMapping = {
  text: TextField,
  number: NumberField,
  date: DateField,
  enum: EnumField
}

export default {
  props: ['value', 'field'],
  data () {
    return { inputValue: this.value }
  },
  methods: {
    fieldTypeToComponent (type) {
      return fieldTypeToComponentMapping[type]
    }
  },
  components: {
    TextField,
    NumberField,
    DateField,
    EnumField
  },
  watch: {
    inputValue (value) {
      this.$emit('input', value)
    }
  }
}
</script>
