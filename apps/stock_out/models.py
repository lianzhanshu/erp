from extensions.models import *


class StockOutOrder(Model):
    """出库单据"""

    class Type(TextChoices):
        """出库类型"""

        SALES = ('sales', '销售')
        PURCHASE_RETURN = ('purchase', '采购退货')

    number = CharField(max_length=32, verbose_name='编号')
    warehouse = ForeignKey('data.Warehouse', on_delete=PROTECT, related_name='stock_out_orders', verbose_name='仓库')
    type = CharField(max_length=32, choices=Type.choices, verbose_name='出库类型')
    sales_order = OneToOneField('sales.SalesOrder', on_delete=CASCADE, null=True,
                                related_name='stock_out_order', verbose_name='销售单据')
    purchase_return_order = OneToOneField('purchase.PurchaseReturnOrder', on_delete=CASCADE, null=True,
                                          related_name='stock_out_order', verbose_name='采购退货单据')
    total_quantity = FloatField(verbose_name='出库总数')
    remain_quantity = FloatField(default=0, verbose_name='出库剩余数量')
    is_completed = BooleanField(default=False, verbose_name='完成状态')
    is_void = BooleanField(default=False, verbose_name='作废状态')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='created_stock_out_orders', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='stock_out_orders')

    class Meta:
        unique_together = [('number', 'team')]

    @classmethod
    def get_number(cls, team):
        start_date, end_date = pendulum.now(), pendulum.tomorrow()
        instance = cls.objects.filter(team=team, create_time__gte=start_date, create_time__lt=end_date).last()

        try:
            result = re.match('^(.*?)([1-9]+)$', instance.number)
            number = result.group(1) + str(int(result.group(2)) + 1)
        except AttributeError:
            number = 'CK' + start_date.format('YYYYMMDD') + '0001'

        return number

class StockOutGoods(Model):
    """出库商品"""

    stock_out_order = ForeignKey('stock_out.StockOutOrder', on_delete=CASCADE,
                                 related_name='stock_out_goods_set', verbose_name='出库单据')
    goods = ForeignKey('goods.Goods', on_delete=PROTECT, related_name='stock_out_goods_set', verbose_name='商品')
    total_quantity = FloatField(verbose_name='出库总数')
    remain_quantity = FloatField(default=0, verbose_name='出库剩余数量')
    is_completed = BooleanField(default=False, verbose_name='完成状态')
    is_void = BooleanField(default=False, verbose_name='作废状态')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='stock_out_goods_set')

    class Meta:
        unique_together = [('stock_out_order', 'goods')]


class StockOutRecord(Model):
    """出库记录"""

    stock_out_order = ForeignKey('stock_out.StockOutOrder', on_delete=CASCADE,
                                 related_name='stock_out_records', verbose_name='出库单据')
    warehouse = ForeignKey('data.Warehouse', on_delete=PROTECT, related_name='stock_out_records', verbose_name='仓库')
    handler = ForeignKey('system.User', on_delete=PROTECT, related_name='stock_out_records', verbose_name='经手人')
    handle_time = DateTimeField(verbose_name='处理时间')
    remark = CharField(max_length=256, null=True, blank=True, verbose_name='备注')
    total_quantity = FloatField(verbose_name='出库总数')
    is_void = BooleanField(default=False, verbose_name='作废状态')
    creator = ForeignKey('system.User', on_delete=PROTECT,
                         related_name='created_stock_out_records', verbose_name='创建人')
    create_time = DateTimeField(auto_now_add=True, verbose_name='创建时间')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='stock_out_records')


class StockOutRecordGoods(Model):
    """出库记录商品"""

    stock_out_record = ForeignKey('stock_out.StockOutRecord', on_delete=CASCADE,
                                 related_name='stock_out_record_goods_set', verbose_name='出库记录')
    stock_out_goods = ForeignKey('stock_out.StockOutGoods', on_delete=CASCADE,
                                 related_name='stock_out_record_goods_set', verbose_name='出库商品')
    goods = ForeignKey('goods.Goods', on_delete=PROTECT, related_name='stock_out_record_goods_set', verbose_name='商品')
    stock_out_quantity = FloatField(default=0, verbose_name='出库数量')
    enable_batch_control = BooleanField(default=False, verbose_name='启用批次控制')
    production_date = DateField(null=True, verbose_name='生产日期')
    shelf_life_days = IntegerField(default=0, verbose_name='保质期天数')
    expiration_date = DateField(null=True, verbose_name='过期日期')
    batch = OneToOneField('goods.Batch', on_delete=CASCADE, null=True,
                          related_name='stock_out_record_goods', verbose_name='批次')
    is_void = BooleanField(default=False, verbose_name='作废状态')
    team = ForeignKey('system.Team', on_delete=CASCADE, related_name='stock_out_record_goods_set')

    class Meta:
        unique_together = [('stock_out_record', 'goods')]


__all__ = [
    'StockOutOrder', 'StockOutGoods',
    'StockOutRecord', 'StockOutRecordGoods',
]
