package cafe.menu;

public class MenuItem {
    private final String name;
    private int price;

    public MenuItem(String name, int price) {
        this.name = name;
        this.price = price;
    }
    public String getName() {
        return name;
    }
    public int getPrice() {
        return price;
    }
}
