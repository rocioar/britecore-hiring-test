import Vue from 'vue'
import Router from 'vue-router'
import RiskTypeList from '@/components/RiskTypeList'
import RiskTypeForm from '@/components/RiskTypeForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'risk-type-list',
      component: RiskTypeList
    },
    {
      path: '/:id',
      name: 'risk-type-form',
      component: RiskTypeForm
    }
  ]
})
