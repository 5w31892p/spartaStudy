package cafe.menu.repository;

import cafe.menu.Menu;
import cafe.menu.MenuItem;

import java.util.HashMap;

public class JavaMenuRepository implements MenuRepository {
    // java를 이용한 데이터베이스(db코드짜는것)

// 1번 방법
//    private List<Menu> menuDB = new ArrayList<>();
//    @Override
//    public void saveMenu(Menu menu) {
//        menuDB.add(menu);
//    }

    private HashMap menuDB = new HashMap();

    // Menu -> CafeMenu, DesertMenu ... 스벅메뉴(1), 투썸메뉴(2)..
    // 위와 같이 메뉴가 많아질 경우 id 부여해야 하므로 HashMap으로 함
    // list도 가능은 함
    @Override
    public void saveMenu(Menu menu) {
        int id = this.menuDB.size() + 1;
        System.out.println("ID : " + id);
        this.menuDB.put(id, menu);
    }

    @Override
    public MenuItem getMenuItem(int menuid, String menuName) {
        Menu menu = (Menu) this.menuDB.get(menuid); // 캐스팅(형변환)을 통해서 Menu임을 알려주는 것
        if (menu == null) throw new IllegalArgumentException("존재하지 않는 메뉴입니다.");
        return menu.getMenuItem(menuName);
    }

    @Override
    public Menu getMenu(int id) {
        Menu menu = (Menu) this.menuDB.get(id);
        if (menu == null) throw new IllegalArgumentException("존재하지 않는 메뉴입니다. 메뉴를 등록하여주세요.");
        return (Menu) this.menuDB.get(id); // id넣어주고 캐스팅해주면 menu 나오는 것
    }
}
