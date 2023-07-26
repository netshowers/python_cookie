from lxml import etree
import xml.etree.ElementTree as ET
import urllib.parse


def main():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
             <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
             <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
             <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
         </ul>
     </div>
    '''

    bookstore = '''
    <bookstore>     
        <book>
          <title lang="eng">Harry Potter</title>
          <price>29.99</price>
        </book>     
        <book>
          <title lang="eng">Learning XML</title>
          <price>39.95</price>
        </book>     
    </bookstore>
    '''

    juzikong = '''
        <div class="list_s2gkX">
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/b5f52ec6-aa1d-4eec-bee9-f50c496cfd12"><img src="https://static.juzicon.com/user/avatar-b5f52ec6-aa1d-4eec-bee9-f50c496cfd12-230619143708-8UJB.jpg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/b5f52ec6-aa1d-4eec-bee9-f50c496cfd12" class="nickname_2OtJR">
                 陌角停落
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/0ebd5983-bddb-4702-97ad-db4ae9900a68"><span><span><span>人一旦悟透了就会变得沉默，不是没有与人相处的能力，而是没有了逢人作戏的兴趣。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/0ebd5983-bddb-4702-97ad-db4ae9900a68#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">88</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">15915</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/87a0203a-ecda-4c1f-ac5f-93ae2e760936"><img src="https://static.juzicon.com/avatars/avatar-190919181531-KNXE.jpg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/87a0203a-ecda-4c1f-ac5f-93ae2e760936" class="nickname_2OtJR">
                 长空当击_581
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/6b05e0d2-23a0-49d9-95fd-37e17d26bcce"><span><span><span>贪安稳就没有自由，要自由就要历些危险。只有这两条路。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/6b05e0d2-23a0-49d9-95fd-37e17d26bcce#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">66</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">13906</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/e5bd3c01-8291-40ec-9ebd-4ede321850f7"><img src="https://static.juzicon.com/user/avatar-e5bd3c01-8291-40ec-9ebd-4ede321850f7-210511105826-EJ8G.jpg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/e5bd3c01-8291-40ec-9ebd-4ede321850f7" class="nickname_2OtJR">
                 Tiger彭珍-
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/97d20ed9-1135-4eef-9aaf-d4922d767c70"><span><span><span>时间，每天得到的都是二十四小时，可是一天的时间给勤勉的人带来智慧和力量，给懒散的人留下一片悔恨。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/97d20ed9-1135-4eef-9aaf-d4922d767c70#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">72</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">8790</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/70018b42-16c7-4524-8384-673bc010f628"><img src="https://static.juzicon.com/avatars/avatar-191123211412-ZLRH.jpeg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/70018b42-16c7-4524-8384-673bc010f628" class="nickname_2OtJR">
                 七年
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/6e3e190b-20c3-47a0-9e78-a504423a93e2"><span><span><span>我曾经尝得，失望无论大小，是一种苦味。</span></span><br></span></a> 
                 <div class="source_18lGW"><a href="/works/f2bce3cd-8053-4691-9e8a-f54e4ca0dd46" target="_blank" class="link_2hHUR"><span><span>《坟》</span></span></a></div>
              </div>
              <div>
                 <a target="_blank" href="/posts/6e3e190b-20c3-47a0-9e78-a504423a93e2#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">28</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">6586</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/54a6b7e1-7c1a-4ffd-9d25-3d200797feaa"><img src="https://static.juzicon.com/avatars/avatar-190922231725-WBJ1.jpeg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/54a6b7e1-7c1a-4ffd-9d25-3d200797feaa" class="nickname_2OtJR">
                 ence
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/effa5202-9be7-47c9-b736-fe21f3056cc8">
                    <span><span><span>勇者愤怒，抽刃向更强者；</span></span><br></span><!----><span><span><span>怯者愤怒，却抽刃向更弱者。</span></span><br></span>
                 </a>
                 <div class="source_18lGW"><a href="/works/43337a0b-2a8d-486e-af95-3f7006514433" target="_blank" class="link_2hHUR"><span><span>《华盖集・杂感》</span></span></a></div>
              </div>
              <div>
                 <a target="_blank" href="/posts/effa5202-9be7-47c9-b736-fe21f3056cc8#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">23</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">5111</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/19fe3f29-9727-4e88-b74f-f23430f8e61d"><img src="https://static.juzicon.com/user/avatar-19fe3f29-9727-4e88-b74f-f23430f8e61d-210328092642-MDPC.jpg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/19fe3f29-9727-4e88-b74f-f23430f8e61d" class="nickname_2OtJR">
                 邀請您及時行樂
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/0aaf8f2b-c881-4546-a851-44b96a9ed0f8"><span><span><span>人一旦悟透了就会变得沉默，不是没有与人相处的能力，而是没有了逢人作戏的兴趣。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/0aaf8f2b-c881-4546-a851-44b96a9ed0f8#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">40</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">4984</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/d1d5e437-8ace-4ed6-b3d0-e700af7ded03"><img src="https://static.juzicon.com/avatars/avatar-200906165555-X1FV.jpeg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/d1d5e437-8ace-4ed6-b3d0-e700af7ded03" class="nickname_2OtJR">
                 徒手摘星<img draggable="false" class="ext-emoji" alt="" src="https://cdn.jsdelivr.net/gh/twitter/twemoji@14.0.2/assets/svg/2728.svg">
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/e5108eef-b9fd-4cf5-adba-97e454bd1f5c"><span><span><span>时间就像海绵里的水，只要愿挤，总还是有的。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/e5108eef-b9fd-4cf5-adba-97e454bd1f5c#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">18</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">4706</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/05c3493d-b951-4447-a4b3-b8e778ba835f"><img src="https://static.juzicon.com/avatars/avatar-20220412000042-aii4.jpeg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/05c3493d-b951-4447-a4b3-b8e778ba835f" class="nickname_2OtJR">
                 阴离子
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/efe21e7c-1e17-4076-95ad-708f939cff4b"><span><span><span>希望的花朵可以五颜六色，但必须根植于现实的土壤。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/efe21e7c-1e17-4076-95ad-708f939cff4b#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">10</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">4510</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/15d77a59-787b-4527-9277-ba9a056b9b56"><img src="https://static.juzicon.com/user/avatar-15d77a59-787b-4527-9277-ba9a056b9b56-210511120334-PY3H.jpg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/15d77a59-787b-4527-9277-ba9a056b9b56" class="nickname_2OtJR">
                 rain.
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/1fc9386b-54f3-4474-8b9a-eb54c0ee3f03"><span><span><span>人说，讽刺和冷嘲只隔一张纸，我以为有趣和肉麻也一样。</span></span><br></span></a> 
                 <div class="source_18lGW"><a href="/works/09ca033c-569c-40a7-8a6b-d82f690e2e6e" target="_blank" class="link_2hHUR"><span><span>《朝花夕拾》</span></span></a></div>
              </div>
              <div>
                 <a target="_blank" href="/posts/1fc9386b-54f3-4474-8b9a-eb54c0ee3f03#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">19</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">4433</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
           <section class="post_3C37i">
              <div class="user_26p5j"><a target="_blank" href="/u/63b96525-b6bb-4a53-83e1-ec4d1b6d07e0"><img src="https://static.juzicon.com/avatars/avatar-200906123534-8ECG.jpeg?x-oss-process=image/resize,m_fill,w_100,h_100" width="30" height="30" class="avatar_30uNb"></a> <a href="/u/63b96525-b6bb-4a53-83e1-ec4d1b6d07e0" class="nickname_2OtJR">
                 Ther
                 </a>
              </div>
              <div class="content_2hYZM">
                 <a href="/posts/010ef52b-d6d4-4cd4-9fa1-7e859402a92f"><span><span><span>猛兽总是独行，牛羊才成群结队。</span></span><br></span></a> <!---->
              </div>
              <div>
                 <a target="_blank" href="/posts/010ef52b-d6d4-4cd4-9fa1-7e859402a92f#comments" class="comment_3HBAQ"><i class="fa fa-comment-o icon_2fT36"></i> <span class="number_2AIKU">32</span></a> <span class="like_3pYp8"><i aria-hidden="true" class="fa fa-heart-o icon_FTRFY"></i> <span class="number_3H9Eq">4378</span></span> <span class="share_3XNW3"><i class="iconfont icon-share visible-xs-inline icon_1bDnz"></i> </span> <!---->
              </div>
           </section>
        </div>
    '''

    # html = etree.HTML(text)
    tree = etree.HTML(bookstore)
    # result = html.xpath('//li[1]/a/text()')
    # print(result)
    # result = html.xpath('//li[last()]/a/text()')
    # print(result)
    # result = html.xpath('//li[@class="item-inactive"]/a/text()')
    # print(result)
    #
    # result = html.xpath('//li[position()<3]/a/text()')
    # print(result)
    # result = html.xpath('//li[last()-2]/a/text()')
    # print(result)

    result = tree.xpath('(//title)[2][@lang]/text()')
    print(result)
    result = tree.xpath('(//title)[2]/@lang')
    print(result)
    result = tree.xpath('(//title)[2]/text()')
    print(result)
    result = tree.xpath('//bookstore/book[price<30]/title/text()')
    print(result)

    juzi = etree.HTML(juzikong)
    result = juzi.xpath('(//img)[2]/@src')
    print(result)
    # result = juzi.xpath("(//span[contains(@class,'number')]/text()")
    result = juzi.xpath(".//span[contains(@class,'number')]/text()")[1].strip()
    print(result)
    base_url = "https://www.juzikong.com"
    div_list = juzi.xpath(".//div[contains(@class,'list')]/section")
    # print(div_list)
    for section in div_list:
        # print(etree.tostring(section, encoding="utf-8").decode())
        relative_url = section.xpath(".//div[contains(@class,'content')]/a/@href")[0]
        nickname = section.xpath(".//a[contains(@class,'nickname')]/text()")[0].strip()
        content = section.xpath(".//div[contains(@class,'content')]//span/text()")[0]
        full_url = urllib.parse.urljoin(base_url, relative_url)
        comment_count = section.xpath(".//a[contains(@class,'comment')]/span/text()")[0]
        like_count = section.xpath(".//span[contains(@class,'like')]/span/text()")[0]
        item = {'name': nickname, 'content': content, 'source': full_url, 'comment': comment_count, 'like': like_count}
        print(item)


if __name__ == '__main__':
    main()
