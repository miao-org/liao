# 滑动变廖器

**[在线玩 →](https://miao-org.github.io/liao/)**

牢廖 ↔ 廖佬 ↔ 廖吊 ↔ 廖圣。

按住头像，左右拖动。表情随滑块位置变化。支持鼠标、手机触摸，以及键盘左右键。

下载 `index.html` 后双击即可使用；所有 JavaScript 和表情图片均已内嵌，无需网络、服务器、安装或构建。支持 WebGL 的浏览器会显示 3D 装置，无法使用 WebGL 时提供简洁滑条。

## 修改

编辑 `page.html`，然后运行 `python3 build.py`，重新生成单文件 `index.html`。`expressions.png` 是四格表情图集，依次为哭丧、自信、狂笑、飞升。

3D 使用 Three.js r160，许可证见 [THREE-LICENSE.txt](THREE-LICENSE.txt)。

表情使用内置 imagegen 工具，根据用户提供的 `portrait.jpg` 制作，提示词见 [expression-prompt.txt](expression-prompt.txt)。图片是幽默表情编辑。

## 已验证

- 在断网的 Chrome 浏览器中直接打开 `file://` 页面，无网络请求或 JavaScript 错误。
- 鼠标拖动切换四档，四张表情互不相同，点击空白处保持状态。
- 390 × 844 手机视口中触摸拖动正常，无横向溢出。
