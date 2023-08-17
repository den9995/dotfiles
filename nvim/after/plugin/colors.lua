function SetMyColorScheme(color)
    color = color or "desert"
    vim.cmd.colorscheme(color)
    vim.api.nvim_set_hl(0,"Normal",     {bg="none"})
    vim.api.nvim_set_hl(0,"NormalFloat",{bg="none"})
    vim.api.nvim_set_hl(0,"NonText",    {bg="none", fg="none"})
end

--SetMyColorScheme("rose-pine-main")
--SetMyColorScheme("slate")
SetMyColorScheme()

--SetMyColorScheme("evening") --bg not trans
--SetMyColorScheme("ron")     --bg not trans

