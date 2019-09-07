// pages/register/register.js
Page({


  formsubmit: function (e) {
    console.log('获取到的：               ' + e.detail.value.name +'                '+ e.detail.value.password),
    wx.request({

      url: 'http://127.0.0.1:8000/register/',

      data: {
        // 'name':e.detail.value.name,
        'name': e.detail.value.name,
        'password': e.detail.value.password,
        'Sex': e.detail.value.Sex,
        'Age': e.detail.value.Age,
        'Number': e.detail.value.Number,
        'Content': e.detail.value.Content,
      },
      
      header: {
        "content-type": "application/x-www-form-urlencoded"		//使用POST方法要带上这个header
      },
      method: 'POST',


      success: res => {
        // this.setData({
        //   text:res.data
        // })
        if (res.statusCode == 200)
          console.log(res.data),
          this.setData({
            result:res.data
          })
            
      }
    })
    
  },
  go_to_text: function (e) {
    wx.navigateTo({
      url: '../text/text',
    })
  }
,

  /**
   * 页面的初始数据
   */
  data: {
    'result':'尚未注册!'
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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