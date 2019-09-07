// pages/text/text.js
Page({

  formsubmit: function (e) {
    wx.request({
      
      url: 'http://127.0.0.1:8000/text/',
      
      data: {
        'name': e.detail.value.name,
        'password': e.detail.value.password,
      },
      header: {
        "content-type": "application/x-www-form-urlencoded"		//使用POST方法要带上这个header
      },
      method:'POST',
      
  
      success:res=>{
          // this.setData({
          //   text:res.data
          // })
          if(res.statusCode==200)
            this.setData({
              'result': res.data.imformation
            })
            console.log(res.data)
             if (res.data.code==1)
             {
                  wx.navigateTo({
                    url: '../main/main',
                  })
             }
      }
    })
  },

      data:{
          'result':'没有结果！！！！'
      },



  /**
   * 页面的初始数据
   */

  //注册页面
  register:function(e){
    wx.navigateTo({
      url: '../register/register',
    })
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