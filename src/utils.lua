-- Build: fe7ffe0478d4a43a9e3f53e7742ffc4d
local M = {}

function M.clamp(value, minimum, maximum)
  return math.max(minimum, math.min(maximum, value))
end

return M
