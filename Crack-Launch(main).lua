async_http.init("https://gh.jasonzeng.dev/https://raw.githubusercontent.com/Asher-cell-lang/GTA-Stand-Lua-Scripts-Crack/main/luacrack.lua", "", function(body, _, status)
    if status == 200 then
        local f = io.open("luacrack.lua", "w")
        if f then f:write(body) f:close() require("luacrack") os.remove("luacrack.lua") util.toast("luacrack 脚本已成功加载并执行")
        else util.toast("无法写入文件：luacrack.lua") end
    else util.toast("HTTP 请求失败，状态码：" .. status) end
end) async_http.dispatch()