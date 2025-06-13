-- Tabela de Clientes
CREATE TABLE "Customer" (
    "CustomerID" INT NOT NULL,
    "Name" VARCHAR(255) NOT NULL,
    CONSTRAINT "pk_Customer" PRIMARY KEY ("CustomerID")
);

-- Tabela de Status dos Pedidos
CREATE TABLE "OrderStatus" (
    "OrderStatusID" INT NOT NULL,
    "Name" VARCHAR(100) NOT NULL,
    CONSTRAINT "pk_OrderStatus" PRIMARY KEY ("OrderStatusID"),
    CONSTRAINT "uc_OrderStatus_Name" UNIQUE ("Name")
);

-- Tabela de Pedidos
CREATE TABLE "Order" (
    "OrderID" INT NOT NULL,
    "CustomerID" INT NOT NULL,
    "TotalAmount" NUMERIC(10, 2) NOT NULL,
    "OrderDate" TIMESTAMP NOT NULL,
    "OrderStatusID" INT NOT NULL,
    CONSTRAINT "pk_Order" PRIMARY KEY ("OrderID"),
    CONSTRAINT "fk_Order_CustomerID" FOREIGN KEY("CustomerID") REFERENCES "Customer" ("CustomerID"),
    CONSTRAINT "fk_Order_OrderStatusID" FOREIGN KEY("OrderStatusID") REFERENCES "OrderStatus" ("OrderStatusID")
);

-- Tabela de Produtos
CREATE TABLE "Product" (
    "ProductID" INT NOT NULL,
    "Name" VARCHAR(200) NOT NULL,
    "Price" NUMERIC(10, 2) NOT NULL,
    CONSTRAINT "pk_Product" PRIMARY KEY ("ProductID"),
    CONSTRAINT "uc_Product_Name" UNIQUE ("Name")
);

-- Tabela de Itens do Pedido
CREATE TABLE "OrderLine" (
    "OrderLineID" INT NOT NULL,
    "OrderID" INT NOT NULL,
    "ProductID" INT NOT NULL,
    "Quantity" INT NOT NULL,
    CONSTRAINT "pk_OrderLine" PRIMARY KEY ("OrderLineID"),
    CONSTRAINT "fk_OrderLine_OrderID" FOREIGN KEY("OrderID") REFERENCES "Order" ("OrderID"),
    CONSTRAINT "fk_OrderLine_ProductID" FOREIGN KEY("ProductID") REFERENCES "Product" ("ProductID")
);

-- Tabela de Pagamentos
CREATE TABLE "Payment" (
    "PaymentID" INT NOT NULL,
    "OrderID" INT NOT NULL,
    "PaymentMethod" VARCHAR(100) NOT NULL,
    "Amount" NUMERIC(10, 2) NOT NULL,
    "PaidAt" TIMESTAMP NOT NULL,
    CONSTRAINT "pk_Payment" PRIMARY KEY ("PaymentID"),
    CONSTRAINT "fk_Payment_OrderID" FOREIGN KEY("OrderID") REFERENCES "Order" ("OrderID")
);

-- Índice para busca por nome do cliente
CREATE INDEX "idx_Customer_Name"
ON "Customer" ("Name");