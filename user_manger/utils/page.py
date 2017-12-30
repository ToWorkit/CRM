# 分页
class PagerHelper:
  # 总数，页码，当前分页url，页数
  def __init__(self, total_count, current_page, base_url, per_page=10):
    self.total_count = total_count
    self.current_page = current_page
    self.base_url = base_url
    self.per_page = per_page

  # property -> 函数以属性的方式调用(省去括号)
  @property
  def db_start(self): # 起始页
    return (self.current_page - 1) * self.per_page

  @property
  def db_end(self): # 结束页
    return self.current_page * self.per_page

  # 总页
  def total_page(self):
    # divmod 
    # v -> 商
    # a -> 余数
    v, a = divmod(self.total_count, self.per_page)
    # 还得来一页
    if a != 0:
      v += 1
    return v

  # 生成页码html
  def pager_str(self):
    v = self.total_page()

    pager_list = []
    if self.current_page == 1:
      pager_list.append('<a href="javascript: void(0);">上一页</a>')
    else:
      pager_list.append('<a href="%s?p=%s">上一页</a>' % (self.base_url, self.current_page - 1, ))

    # 第6页 -> 页码 1 : 12
    # 第7页 -> 页码 2 : 13
    # 单位为 5
    if v <= 11:
      pager_range_start = 1
      pager_range_end = v
    else:
      if self.current_page < 6:
        pager_range_start = 1
        pager_range_end = 11 + 1
      else:
        pager_range_start = self.current_page - 5
        pager_range_end = self.current_page + 5 + 1
        if pager_range_end > v:
          pager_range_start = v - 10
          pager_range_end = v + 1

    # 生成html
    for i in range(pager_range_start, pager_range_end):
      if i == self.current_page:
        pager_list.append('<a href="%s?p=%s" class="active">%s</a>' % (self.base_url, i, i, ))
      else:
        pager_list.append('<a href="%s?p=%s">%s</a>' % (self.base_url, i, i, ))

    if self.current_page == v:
      pager_list.append('<a href="javascript:;">下一页</a>')
    else:
      pager_list.append('<a href="%s?p=%s">下一页</a>' % (self.base_url, self.current_page + 1))

    pager = ''.join(pager_list)
    return pager


