Page({
  data: {
    imgUrls: [
      'https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=2590572703,1989846887&fm=26&gp=0.jpg',
      'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567342086800&di=5b0a45822dbb0e4cdbe9014bf1efd100&imgtype=0&src=http%3A%2F%2Fimg4.duitang.com%2Fuploads%2Fitem%2F201207%2F12%2F20120712122021_zhZZA.thumb.600_0.jpeg',
      'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567936873&di=67db3828a83ff6461909240a1641242c&imgtype=jpg&er=1&src=http%3A%2F%2Fimage.tianjimedia.com%2FuploadImages%2F2015%2F323%2F20151119105747265009.jpg'
    ]
  ,
    grids: 
    [
        { image: 'https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=4107115519,146325798&fm=26&gp=0.jpg', text: '查看所有用户信息',goto:'../person/person'},
        { image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567522139858&di=f76dec7433879421eb578ce9886cb213&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170503%2F2ed75e64a9cb49248f133fe360351aaa_th.gif', text: '天气预报查询', goto: '../weather/weather'},
        { image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567340698321&di=7b70479fb6ca5fe27d9fcf6c6e95752c&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F02%2F77%2F61%2F5a3a468c8e830_610.jpg', text: '联系我', goto: '../kefu/kefu' },
        { image: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567358582739&di=44cfea4a172650f30dee4c15fe2129a8&imgtype=0&src=http%3A%2F%2Fpic.51yuansu.com%2Fpic3%2Fcover%2F01%2F40%2F78%2F59273cc29de3c_610.jpg', text: '给我留言', goto: '../liuyan/liuyan' }
        
    ]
  }
  
  ,
  text: function (e) {
    wx.navigateTo({
      url: '../text/text',
    })
  }
});