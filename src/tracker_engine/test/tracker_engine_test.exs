defmodule TrackerEngineTest do
  use ExUnit.Case
  doctest TrackerEngine

  test "greets the world" do
    assert TrackerEngine.hello() == :world
  end
end
