var fieldMixin = {
  props: ['value', 'id', 'options'],
  data () {
    return { inputValue: this.value }
  },
  watch: {
    inputValue (value) {
      this.$emit('input', value)
    }
  }
}

export default fieldMixin
