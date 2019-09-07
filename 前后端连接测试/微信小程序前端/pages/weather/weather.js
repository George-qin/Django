// pages/weather/weather.js
Page({

      data: {
        'weather': '',
        'temperature_hight': '',
        'temperature_low': '',
        'wind': ''
      },


      formsubmit: function(e) {

        //console.log(e.detail.value.day, e.detail.value.city)
        wx.request({
            url: 'http://127.0.0.1:8000/weather/',
            data: {
              'day': e.detail.value.day,
              'city': e.detail.value.city
            },

            success: res => {


              console.log(res.data)


              if (res.statusCode == 200) {
                this.setData({
                  'weather': res.data.weather,
                  'temperature_hight': res.data.temperature_hight,
                  'temperature_low': res.data.temperature_low,
                  'wind': res.data.wind
                })
              }
            }
        })


          },


          main: function(e) {
            wx.navigateTo({
              url: '../main/main',
            })
          },

          data: {

          },

          /**
           * 生命周期函数--监听页面加载
           */
          onLoad: function(options) {

          },

          /**
           * 生命周期函数--监听页面初次渲染完成
           */
          onReady: function() {

          },

          /**
           * 生命周期函数--监听页面显示
           */
          onShow: function() {

          },

          /**
           * 生命周期函数--监听页面隐藏
           */
          onHide: function() {

          },

          /**
           * 生命周期函数--监听页面卸载
           */
          onUnload: function() {

          },

          /**
           * 页面相关事件处理函数--监听用户下拉动作
           */
          onPullDownRefresh: function() {

          },

          /**
           * 页面上拉触底事件的处理函数
           */
          onReachBottom: function() {

          },

          /**
           * 用户点击右上角分享
           */
          onShareAppMessage: function() {

          }
        })