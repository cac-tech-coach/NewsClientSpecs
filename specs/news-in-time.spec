# 随时随地看到最新的新闻

作为用户
我希望随时随地可以看到最新的新闻
以便于关注一些突发事件

## 新闻列表预加载

* 如果第一个新闻栏目Tab"头条"的新闻列表已经展示出来
* 当用户切换到最后一个新闻栏目Tab"科技"时
* 那么他应该看到"科技"栏目下的新闻列表立即展现出来
* 当用户切换到第二个新闻栏目Tab"体育"时
* 那么他应该看到"体育"栏目下的新闻列表立即展现出来

## 离线浏览新闻

* 如果用户之前打开应用时已经获取过新闻栏目和新闻列表
* 如果任何问题导致新闻栏目和新闻列表无法获取
* 当用户再次打开应用时
* 那么用户应该看到新闻栏目和新闻列表加载出来
* 而且新闻栏目和新闻列表的内容和上一次打开应用时看到的一样

## 下拉刷新看到更多的新闻

* 如果新闻列表已经展示出来，不管是不分类的新闻列表还是Tab下的新闻列表
* 当用户向上滚动到列表的顶端
* 并且他再次向下拉动列表并松开后
* 那么他应该看到新的新闻被加载出来
* 并且新的新闻被依次附加在新闻列表的顶端

## 已经是最新时下拉刷新

* 如果新闻列表已经展示出来，不管是不分类的新闻列表还是Tab下的新闻列表
* 并且新闻列表中的内容已经是最新
* 当用户下拉刷新时
* 那么用户应该看到"没有更新的新闻了"的提示
* 并且他不应该看到原来的新闻列表发生任何变化

## 下拉刷新时出错

* 如果新闻列表已经展示出来，不管是不分类的新闻列表还是Tab下的新闻列表
* 并且这时新闻加载过程中出现问题
* 当用户下拉刷新时
* 那么用户应该看到"最新新闻无法加载"的提示
* 并且他不应该看到原来的新闻列表发生任何变化

