# Raspberry Piでロボットをつくろう！ - コードリポジトリ

[![表紙](images/cover-thumbnail.png)](https://www.kyoritsu-pub.co.jp/bookdetail/9784320124813)

## このリポジトリの説明

このリポジトリは，『[Learn Robotics with Raspberry Pi: Build and Code Your Own Moving, Sensing, Thinking Robots](https://nostarch.com/raspirobots/)』（Matt Timmons-Brown著，[No Starch Press](https://nostarch.com/)，2019年）を翻訳した『[Raspberry Piでロボットをつくろう！—動いて，感じて，考えるロボットの製作とPythonプログラミング—](https://www.kyoritsu-pub.co.jp/bookdetail/9784320124813)』（齊藤哲哉訳，[共立出版](https://www.kyoritsu-pub.co.jp/)，2021年）のコードリポジトリです。

原著のコードリポジトリである[https://github.com/the-raspberry-pi-guy/raspirobots](https://github.com/the-raspberry-pi-guy/raspirobots)で公開されているソースコードのうち，訳本で翻訳した部分を含めて公開しています。

また，訳本を読むうえで参考になる情報や正誤情報も公開していきます。

## 部品表

[Supply chain, shortages, and our first-ever price increase](https://www.raspberrypi.com/news/supply-chain-shortages-and-our-first-ever-price-increase/)（「サプライチェン，欠品，そして初めての値上げ」，2021年10月20日）に書かれている通り，世界的な半導体不足のため，Raspberry Piが手に入りにくい状況が続いています。特に，本書で使っているRaspberry Pi 3B+に関しては，一時的ですが他のモデル（Pi 3B，Compute Module 3/3+）の生産を優先する措置が取られています。しばらくはRaspberry Pi 3Bの方が入手しやすい状況が続くと思われますので，3Bを入手することをお勧めします。

※販売状況は2021年12月26日現在

<table>
    <thead>
        <tr>
            <th>部品</th>
            <th>購入先</th>
            <th>販売状況</th>
        </tr>
    </thaed>
    <tbody>
        <tr>
            <td rowspan=6>Raspberry Pi 3 Model B+スターターキット</td>
            <td><a href="https://ssci.to/3880">https://ssci.to/3880</a></td>
            <td>販売終了</td>
        </tr>
        <tr>
            <td>
                白，16GB <a href="https://raspberry-pi.ksyic.com/main/index/pdp.id/446/pdp.open/446">https://raspberry-pi.ksyic.com/main/index/pdp.id/446/pdp.open/446</a>
            </td>
            <td>入荷未定</td>
        </tr>
        <tr>
            <td>
                黒，16GB <a href="https://raspberry-pi.ksyic.com/main/index/pdp.id/447/pdp.open/447">https://raspberry-pi.ksyic.com/main/index/pdp.id/447/pdp.open/447</a>
            </td>
            <td>入荷未定</td>
        </tr>
        <tr>
            <td>
                透明，16GB <a href="https://raspberry-pi.ksyic.com/main/index/pdp.id/448/pdp.open/448">https://raspberry-pi.ksyic.com/main/index/pdp.id/448/pdp.open/448</a>
            </td>
            <td>入荷未定</td>
        </tr>
        <tr>
            <td>
            赤，16GB <a href="https://raspberry-pi.ksyic.com/main/index/pdp.id/449/pdp.open/449">https://raspberry-pi.ksyic.com/main/index/pdp.id/449/pdp.open/449</a>
            </td>
            <td>入荷未定</td>
        </tr>
        <tr>
            <td>
                透明，32GB <a href="https://raspberry-pi.ksyic.com/main/index/pdp.id/438/pdp.open/438">https://raspberry-pi.ksyic.com/main/index/pdp.id/438/pdp.open/438</a>
            </td>
            <td>入荷未定</td>
        </tr>
        <tr>
            <td rowspan=4>Raspberry Pi 3 Model B</td>
            <td>
                <a href="https://ssci.to/3050">https://ssci.to/3050</a>
            </td>
            <td>入荷未定</td>
        </tr>
        <tr>
            <td>
                <a href="https://www.yodobashi.com/product/100000001003445642/">https://www.yodobashi.com/product/100000001003445642/</a>（アイ･オー･データ製）
            </td>
            <td>在庫なし</td>
        </tr>
        <tr>
            <td>
                <a href="https://www.marutsu.co.jp/pc/i/834053/">https://www.marutsu.co.jp/pc/i/834053/</a>
            </td>
            <td>入荷待ち</td>
        </tr>
        <tr>
            <td>
                <a href="https://akizukidenshi.com/catalog/g/gM-10414/">https://akizukidenshi.com/catalog/g/gM-10414/</a>
            </td>
            <td>在庫あり</td>
        </tr>
        <tr>
          <td>
            公式 Raspberry Piカメラモジュール
          </td>
          <td>
            <a href="https://ssci.to/2713">https://ssci.to/2713</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            公式 Raspberry Piオフィシャルマウス
          </td>
          <td>
            <a href="https://ssci.to/6426">https://ssci.to/6426</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            公式 Raspberry Piオフィシャルキーボード
          </td>
          <td>
            <a href="https://ssci.to/6425">https://ssci.to/6425</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            400穴ブレッドボード
          </td>
          <td>
            <a href="https://ssci.to/313">https://ssci.to/313</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            抵抗コンデンサLED詰め合わせパック
          </td>
          <td>
            <a href="https://ssci.to/1218">https://ssci.to/1218</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td rowspan=3>
            ジャンパワイヤー
          </td>
          <td>
            オス-メス <a href="https://ssci.to/209">https://ssci.to/209</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
            <td>
                メス-メス <a href="https://ssci.to/56">https://ssci.to/56</a>
            </td>
            <td>
                在庫あり
            </td>
        </tr>
        <tr>
            <td>
            オス-オス <a href="https://ssci.to/57">https://ssci.to/57</a>
            </td>
            </td>
            <td>
                在庫あり
            </td>
        </tr>
        <tr>
          <td>
            モーメンタリ式押しボタン
          </td>
          <td>
            <a href="https://ssci.to/38">https://ssci.to/38</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            電池ホルダー（単三×6）
          </td>
          <td>
            <a href="https://www.marutsu.co.jp/pc/i/65884/">https://www.marutsu.co.jp/pc/i/65884/</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            降圧コンバータ（LM2596）
          </td>
          <td>
            <a href="https://www.marutsu.co.jp/pc/i/25649540/">https://www.marutsu.co.jp/pc/i/25649540/</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            モーターコントローラチップ（L293D）
          </td>
          <td>
            <a href="https://www.marutsu.co.jp/pc/i/13014388/">https://www.marutsu.co.jp/pc/i/13014388/</a>
          </td>
          <td>
            在庫なし
          </td>
        </tr>
        <tr>
          <td>
            JetBot Chassis Kit V2
          </td>
          <td>
            <a href="https://ssci.to/6944">https://ssci.to/6944</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            Wiiリモコン
          </td>
          <td>
            中古 <a href="https://item.rakuten.co.jp/iimoreuse/169/">https://item.rakuten.co.jp/iimoreuse/169/</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            超音波距離センサー（HC-SR04）
          </td>
          <td>
            <a href="https://ssci.to/6080">https://ssci.to/6080</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            抵抗キット 1/4W（20種計500本入り）
          </td>
          <td>
            <a href="https://ssci.to/1084">https://ssci.to/1084</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td rowspan=2>
            NeoPixel Stick
          </td>
          <td>
            本体 <a href="https://www.marutsu.co.jp/pc/i/829719/">https://www.marutsu.co.jp/pc/i/829719/</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            ピンヘッダ <a href="https://www.marutsu.co.jp/pc/i/60528/">https://www.marutsu.co.jp/pc/i/60528/</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            3.5mmスピーカー
          </td>
          <td>
            <a href="https://amazon.jp/dp/B075NXYGKX">https://amazon.jp/dp/B075NXYGKX</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
        <tr>
          <td>
            線追従センサー（TCRT5000ベース）
          </td>
          <td>
            <a href="https://store.shopping.yahoo.co.jp/stk-shop/73010615.html">https://store.shopping.yahoo.co.jp/stk-shop/73010615.html</a>
          </td>
          <td>
            在庫あり
          </td>
        </tr>
    </tbody>
</table>


## 正誤表

訳本に間違いを見つけた場合はPRを送るか，saito.tetsuya[at]gmail.comにメールしてください。

