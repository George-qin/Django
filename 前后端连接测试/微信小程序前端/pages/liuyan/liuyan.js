// pages/liuyan/liuyan.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  subumit:function(e){
    wx.request({
      url: 'http://127.0.0.1:8000/LiuYan/',
      data:{
        'saying': e.detail.value.saying,
        'name': e.detail.value.name
      },
      header: {
        "content-type": "application/x-www-form-urlencoded"		//使用POST方法要带上这个header
      },
      method: 'POST'
      ,
      success: res => {
        if (res.statusCode == 200) {
            console.log(  res.data)
        }
      }
      
  


    })//请求结尾
    

  },//事件动作结尾


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    wx.request({
      url: 'http://127.0.0.1:8000/check/',
      success: res => {
        if (res.statusCode == 200) {
          console.log(res.data)
          
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})