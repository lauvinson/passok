
        function showIframe(url,w,h){
            //添加iframe
            var if_w = w;
            var if_h = h;
            $("<iframe width='" + if_w + "' height='" + if_h + "' id='iFrame' name='iFrame' style='position:absolute;z-index:4;' frameborder='no' scrolling='no' allowtransparency='yes' security='restricted' sandbox='allow-top-navigation allow-same-origin allow-forms allow-scripts' marginheight='0' marginwidth='0' allowTransparency='true'></iframe>").prependTo('body');
            //iframe屏幕适应宽高设置
            var st=document.documentElement.scrollTop|| document.body.scrollTop;//滚动条距顶部的距离
            var sl=document.documentElement.scrollLeft|| document.body.scrollLeft;//滚动条距左边的距离
            var ch=document.documentElement.clientHeight;//屏幕的高度
            var cw=document.documentElement.clientWidth;//屏幕的宽度
            var objH=$("#iFrame").height();//浮动对象的高度
            var objW=$("#iFrame").width();//浮动对象的宽度
            var objT=Number(st)+(Number(ch)-Number(objH))/2;
            var objL=Number(sl)+(Number(cw)-Number(objW))/2;
            $("#iFramee").css('left',objL);
            $("#iFrame").css('top',objT);
            $("#iFrame").attr("src", url)
        };

        function test(i) {
        if (i < document.getElementsByClassName('job-list-box')[0].childNodes.length) {
            try {
                showIframe(document.getElementsByClassName('job-list-box')[0].childNodes[i].firstChild.firstChild.href,'100%','100%');
            }catch (e) {

            }
            setTimeout(function() {
                document.getElementById('iFrame').remove()
                test(i + 1);
            }, 3000)
        } else {
            console.log('翻页')
            //翻页
            document.getElementsByClassName('options-pages')[0].childNodes[document.getElementsByClassName('options-pages')[0].childNodes.length - 1].click()
            setTimeout(function(){
                test(0)
            }, 3000)
        }
        }

        test(0)