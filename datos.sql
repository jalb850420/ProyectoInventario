insert into Clientes (id, nombre, apellidos, telefono)
  values('109899', 'Juan', 'Pérez Gómez', 3023345664);
insert into Clientes (id, nombre, apellidos, telefono)
  values('104695', 'José', 'López Ariza', 3123675774);

insert into FormaDePago (id, nombre) 
  values(1, 'Tarjeta de crédito');
insert into FormaDePago (id, nombre) 
  values(2, 'Tarjeta dédito');
insert into FormaDePago (id, nombre) 
  values(3, 'Efectivo');

insert into Producto (id, nombre, precio, existencia)
  values('99', 'Mouse', 25000, 64);
insert into Producto (id, nombre, precio, existencia)
  values('104', 'Teclado', '48000', 77);
insert into Producto (id, nombre, precio, existencia)
  values('47', 'Monitor', '368000', 23);

insert into Pedido (id, id_cliente, fecha, id_forma_pago) 
  values(1008, 109899, '6/12/20', 2);
insert into Pedido (id, id_cliente, fecha, id_forma_pago) 
  values(1009, 109899, '23/11/20', 3);
insert into Pedido (id, id_cliente, fecha, id_forma_pago) 
  values(1018, 104695, '1/12/20', 2);

  insert into DetallePedido (sec, id_pedido, id_producto, precio, cantidad)
  values(1, 1008, 104, 48000, 2);
insert into DetallePedido (sec, id_pedido, id_producto, precio, cantidad)
  values(2, 1018, 104, 48000, 4);
insert into DetallePedido (sec, id_pedido, id_producto, precio, cantidad)
  values(3, 1009, 47, 368000, 1);

