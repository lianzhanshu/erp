import request from '@/utils/request';


// RoleOption
export function roleOption(params) {
  return request({ url: `/roles/options/`, method: 'get', params })
}

// UserOption
export function userOption(params) {
  return request({ url: `/users/options/`, method: 'get', params })
}

// 商品
export function materialsOption(params) {
  return request({ url: `/materials/options/`, method: 'get', params })
}
// 供应商分类
export function supplierClassification(params) {
  return request({ url: `/supplier_categories/options/`, method: 'get', params })
}
// 供应商
export function suppliersOption(params) {
  return request({ url: `/suppliers/options/`, method: 'get', params })
}
// 客户分类
export function clientClassification(params) {
  return request({ url: `/client_categories/options/`, method: 'get', params })
}
// 客户
export function clientsOption(params) {
  return request({ url: `/clients/options/`, method: 'get', params })
}
// 仓库
export function warehousesOption(params) {
  return request({ url: `/warehouses/options/`, method: 'get', params })
}
// 商品分类
export function goodsClassificationOption(params) {
  return request({ url: `/goods_categories/options/`, method: 'get', params })
}
// 商品单位
export function goodsUnitOption(params) {
  return request({ url: `/goods_units/options/`, method: 'get', params })
}
// 商品选项
export function inventoriesOption(params) {
  return request({ url: `/inventories/options/`, method: 'get', params })
}
// 结算账户
export function accountsOption(params) {
  return request({ url: `/accounts/options/`, method: 'get', params })
}
// 采购单据
export function purchaseOrdersOption(params) {
  return request({ url: `/purchase_orders/options/`, method: 'get', params })
}
// // 业务经理
// export function managerOption(params) {
//   return request({ url: `/users/options/`, method: 'get', params })
// }
// // 合同
// export function contractOption(params) {
//   return request({ url: `/contract_orders/options/`, method: 'get', params })
// }

// // 合同原料
// export function contractMaterialsOption(params) {
//   return request({ url: `/contract_materials/options/`, method: 'get', params })
// }

// // 采购单原料
// export function purchaseMaterialsOption(params) {
//   return request({ url: `/purchase_materials/options/`, method: 'get', params })
// }

// // 装箱清单
// export function packingOrdersOption(params) {
//   return request({ url: `/packing_orders/options/`, method: 'get', params })
// }

// // 装箱清单原料
// export function packingMaterialsOption(params) {
//   return request({ url: `/packing_materials/options/`, method: 'get', params })
// }
